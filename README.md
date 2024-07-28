## STEPS TO RUN THE CODE ON DOCKER

1. Step 1 :
    - Build Docker Image For Promptflow API with command" docker build -t sudoku-telegram-promptflow ./SudokuPromptFlowDocker/ "

2. Step 2 :
    - Build Docker Image For TelegramBot with command" docker build -t sudoku-telegram-bot ./SudokuPromptFlowDocker/ "

3. Step 3 : 
    - Use the Docker Compose to run these images together on the same network using " docker compose up " 