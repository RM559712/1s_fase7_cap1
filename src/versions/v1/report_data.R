if (!require(rjson)) install.packages("rjson")
library(rjson)

tryCatch({

  cat('\n')
  cat('Resultados a partir das culturas e cálculos\n')
  cat('-------------------------------------------\n')
  cat('\n')

  # Processo de "reset" de variáveis
  rm(list = ls())

  # Processo de definição do diretório que o script deverá ser executado
  args <- commandArgs(trailingOnly = FALSE)
  script_path <- sub("--file=", "", args[grep("--file=", args)])
  script_dir <- dirname(script_path)
  if(length(script_dir) == 0) script_dir <- getwd()

  # Processo de validação do arquivo contendo os dados
  full_path <- paste0(script_dir,"/data/_tempData.json")
  if(file.exists(full_path) == FALSE) stop('Não foi possível concluir o processo pois o arquivo de dados não existe.')
  file_data_calcs = full_path
  
  # Processo de abertura do arquivo
  json_data_calcs <- fromJSON(file=file_data_calcs)
  if (length(json_data_calcs) == 0) stop('Não existem dados para serem calculados.')
  
  cat('Os itens abaixo estão agrupados por cultura e cálculo.\n\n')

  # Processo de agrupamento dos dados utilizando como parâmetro:
  # - Código da cultura
  # - Código do cálculo
  list_data_calcs = list()
  
  for (key in 1:length(json_data_calcs)) {
    
    crop_code = as.character(json_data_calcs[[key]]$code)
    crop = json_data_calcs[[key]]$crop
    calc_code = as.character(json_data_calcs[[key]]$calc$code)
    calc = json_data_calcs[[key]]$calc$title
    
    # > Regras: A validação abaixo armazena o valor final do cálculo pois cada cálculo possui uma estrutura diferente de saída
    result_calc = 0
    if(calc_code == '1') result_calc = json_data_calcs[[key]]$calc$result_calc$total_area_m2
    else if(calc_code == '2') result_calc = json_data_calcs[[key]]$calc$result_calc$total_area_m2
    else if(calc_code == '3') result_calc = json_data_calcs[[key]]$calc$result_calc$number_streets
    else if(calc_code == '4') result_calc = json_data_calcs[[key]]$calc$result_calc$number_plants
    else if(calc_code == '5') result_calc = json_data_calcs[[key]]$calc$result_calc$number_input_street
    else if(calc_code == '6') result_calc = json_data_calcs[[key]]$calc$result_calc$total_input
    
    crop_calc_code = paste0(crop_code, '_', calc_code)
    
    list_data_calcs[[crop_calc_code]][['crop']] <- crop
    list_data_calcs[[crop_calc_code]][['calc']] <- calc
    list_data_calcs[[crop_calc_code]][['results']] = append(list_data_calcs[[crop_calc_code]][['results']], result_calc)
    
  }
  
  for (key in 1:length(list_data_calcs)) {

    media = mean(list_data_calcs[[key]]$results)
    desvio = sd(list_data_calcs[[key]]$results)

    if(key > 1) cat('\n')
    cat('> Cultura:', list_data_calcs[[key]]$crop, '\n')
    cat('- Cálculo:', list_data_calcs[[key]]$calc, '\n')
    cat('- Quantidade de resultados:', length(list_data_calcs[[key]]$results), '\n')
    cat('- Média:', media, '\n')
    cat('- Desvio:', desvio, '\n')

  }

}, error = function(e) {

  cat('> Ocorreu o seguinte erro:', e$message)

})