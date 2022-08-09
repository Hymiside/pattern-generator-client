# Модуль service
Модуль обрабатывает бизнес логику на клиенте.
## Методы
1. **user_status** – метод проверяет существует ли пользователь в базе по user_id Telegram. <br/>

Ответы
```json
{
  "status": "user does not exist / user already exists / error"
}
```

<br/>

2. **get_balance** – метод возвращает баланс пользователя по user_id Telegram. <br/>

Ответ cо статусом *200*
```json
{
  "status": "ok",
  "balance": "350"
}
```
Ответ cо статусом *400/500*
```json
{
  "status": "error",
  "balance": "-"
}
```