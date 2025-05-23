# Script to connect to Open Meteo to collect Meteo Forecasts (7 days)
# 09 Sept 2024 - Marco Franzoi - v1.1

# Install and load required packages
if (!require(httr)) install.packages("httr")
if (!require(jsonlite)) install.packages("jsonlite")
library(httr)
library(jsonlite)
library(stringr)

# Function to test server connection
test_connection <- function(url) {
  tryCatch({
    response <- GET(url, timeout(5))
    if (status_code(response) == 200) {
      cat("Conexão com o servidor bem-sucedida.\n\n")
      return(TRUE)
    } else {
      cat("Falha na conexão com o servidor. Código de status:", status_code(response), "\n")
      return(FALSE)
    }
  }, error = function(e) {
    cat("Erro ao conectar ao servidor:", conditionMessage(e), "\n")
    return(FALSE)
  })
}

# Test connection to the server
base_url <- "https://api.open-meteo.com/v1/forecast"
if (!test_connection(base_url)) {
  cat("O script será encerrado devido a falha na conexão.\n")
  quit(status = 1)
}

# Set coordinates for São Paulo, Brazil
latitude <- -23.5505
longitude <- -46.6333

# Construct the API URL
query_params <- list(
  latitude = latitude,
  longitude = longitude,
  daily = "temperature_2m_max,temperature_2m_min,precipitation_sum",
  timezone = "America/Sao_Paulo",
  forecast_days = 7
)

# Define weather symbols
sun_symbol <- "\u2600"  # ☀️
rain_symbol <- "\u2614"  # ☔

# Function to determine weather symbol
get_weather_symbol <- function(max_temp, precipitation) {
  if (precipitation > 0) {
    return(rain_symbol)
  } else if (max_temp >= 25) {
    return(sun_symbol)
  } else {
    return("")
  }
}

# Portuguese weekday names
dias_semana <- c("Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb")

# Portuguese month names
meses <- c("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")

# Make the API request
response <- GET(base_url, query = query_params)

# Check the response
if (status_code(response) == 200) {
  # Parse the JSON response
  data <- fromJSON(content(response, "text", encoding = "UTF-8"))
  
  # Extract the forecast data
  forecast <- data.frame(
    Date = as.Date(data$daily$time),
    Max_Temp = data$daily$temperature_2m_max,
    Min_Temp = data$daily$temperature_2m_min,
    Precipitation = data$daily$precipitation_sum
  )
  
  # Format dates in Portuguese
  formatted_dates <- sapply(forecast$Date, function(d) {
    paste(dias_semana[as.POSIXlt(d)$wday + 1],
          format(d, "%d"),
          meses[as.POSIXlt(d)$mon + 1],
          format(d, "%y"))
  })
  
  # Print the forecast in a columnar format
  cat("Previsão do Tempo para 7 Dias em São Paulo, Brasil\n")
  cat("--------------------------------------------------\n\n")
  
  # Print header
  cat(sprintf("%-18s %-15s %-15s %-15s %-10s\n", "Data", "Temp Máx (°C)", "  Temp Mín (°C)", "  Precip (mm)", "  Clima"))
  cat(sprintf("%-18s %-15s %-15s %-15s %-10s\n", "----", "-------------", "-------------", "------------", "-----"))
  
  # Print data rows
  for (i in 1:nrow(forecast)) {
    weather_symbol <- get_weather_symbol(forecast$Max_Temp[i], forecast$Precipitation[i])
    cat(sprintf("%-18s %-15.1f %-15.1f %-15.1f %-10s\n",
                str_pad(formatted_dates[i], 18, 'right', ' '),
                forecast$Max_Temp[i],
                forecast$Min_Temp[i],
                forecast$Precipitation[i],
                weather_symbol))
  }
  
  cat("\n")
  
  # Print summary statistics
  cat("Resumo Estatístico:\n")
  cat("-------------------\n")
  cat(sprintf("Temperatura Máxima Média: %.1f°C\n", mean(forecast$Max_Temp)))
  cat(sprintf("Temperatura Mínima Média: %.1f°C\n", mean(forecast$Min_Temp)))
  cat(sprintf("Precipitação Total:       %.1f mm\n", sum(forecast$Precipitation)))
  
} else {
  cat("Erro: Não foi possível recuperar os dados. Código de status:", status_code(response), "\n")
}