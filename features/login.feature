Feature: Login do Sistema
  Como um usuário do sistema
  Eu quero fazer login
  Para acessar as funcionalidades protegidas

  Scenario: Login com sucesso
    Given que estou na página de login
    When eu preencho o campo "username" com "usuario@teste.com"
    And eu preencho o campo "password" com "senha123"
    And eu clico no botão "Entrar"
    Then eu devo ver a mensagem "Login realizado com sucesso"

  Scenario: Login com credenciais inválidas
    Given que estou na página de login
    When eu preencho o campo "username" com "usuario@invalido.com"
    And eu preencho o campo "password" com "senha_errada"
    And eu clico no botão "Entrar"
    Then eu devo ver a mensagem "Credenciais inválidas"
