# Install and load required packages
if (!require(httr)) install.packages("httr")
if (!require(jsonlite)) install.packages("jsonlite")
library(httr)
library(jsonlite)
library(stringr)

# Define the cities and their coordinates
cities <- list(
  "1" = list(name = "São Paulo, SP", coords = c(-23.5505, -46.6333)),
  "2" = list(name = "Sorriso, MT", coords = c(-12.5370, -55.4355)),
  "3" = list(name = "Patrocínio, MG", coords = c(-20.2641, -46.9889)),
  "4" = list(name = "Uruguaiana, RS", coords = c(-29.9700, -57.0886))
)

# Function to display the menu and get user choice
get_city_choice <- function() {
  cat("Escolha uma cidade:\n")
  for (key in names(cities)) {
    cat(paste0(key, ". ", cities[[key]]$name, "\n"))
  }
  while (TRUE) {
    choice <- readline("Digite o número da cidade desejada: ")
    if (choice %in% names(cities)) {
      return(cities[[choice]])
    }
    cat("Escolha inválida. Por favor, tente novamente.\n")
  }
}

# Function to fetch weather data
fetch_weather_data <- function(latitude, longitude) {
  base_url <- "https://api.open-meteo.com/v1/forecast"
  query_params <- list(
    latitude = latitude,
    longitude = longitude,
    daily = "temperature_2m_max,temperature_2m_min,precipitation_sum",
    timezone = "America/Sao_Paulo",
    forecast_days = 7
  )
  response <- GET(base_url, query = query_params)
  if (status_code(response) == 200) {
    return(fromJSON(content(response, "text", encoding = "UTF-8")))
  } else {
    stop("Erro ao recuperar dados meteorológicos. Código de status: ", status_code(response))
  }
}

# Function to display the forecast
display_forecast <- function(city_name, weather_data) {
  forecast <- weather_data$daily
  
  dias_semana <- c("Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb")
  meses <- c("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")
  
  cat(paste0("\nPrevisão do Tempo para 7 Dias em ", city_name, "\n"))
  cat("--------------------------------------------------\n\n")
  cat(sprintf("%-18s %-15s %-15s %-15s\n", "Data", "Temp Máx (°C)", "Temp Mín (°C)", "Precip (mm)"))
  cat(sprintf("%-18s %-15s %-15s %-15s\n", "----", "-------------", "-------------", "------------"))
  
  for (i in 1:length(forecast$time)) {
    date <- as.POSIXlt(forecast$time[i])
    formatted_date <- paste(
      dias_semana[date$wday + 1],
      sprintf("%02d", date$mday),
      meses[date$mon + 1],
      substr(date$year + 1900, 3, 4)
    )
    cat(sprintf("%-18s %-15.1f %-15.1f %-15.1f\n",
                str_pad(formatted_date, 18, 'right', ' '),
                forecast$temperature_2m_max[i],
                forecast$temperature_2m_min[i],
                forecast$precipitation_sum[i]))
  }
  
  cat("\nResumo Estatístico:\n")
  cat("-------------------\n")
  cat(sprintf("Temperatura Máxima Média: %.1f°C\n", mean(forecast$temperature_2m_max)))
  cat(sprintf("Temperatura Mínima Média: %.1f°C\n", mean(forecast$temperature_2m_min)))
  cat(sprintf("Precipitação Total:       %.1f mm\n", sum(forecast$precipitation_sum)))
}

# Main program loop
while (TRUE) {
  city <- get_city_choice()
  weather_data <- fetch_weather_data(city$coords[1], city$coords[2])
  display_forecast(city$name, weather_data)
  
  continue <- tolower(readline("\nDeseja consultar outra cidade? (S/N): "))
  if (continue != "s") {
    break
  }
}

cat("Obrigado por usar o serviço de previsão do tempo!\n")