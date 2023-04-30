# Django user api

- Register api: User having following fields: `username`, `password`, `mobile`, `name`, `address`, `email` ( validation ie username consist of alphabets only, mobile integer with length 10,email
validation, password should contains alphnumeric and some special character. Once user created email triggered to email id with password details. This user information is stored into database. On successful insertion userid which should be auto generated should be return.

- Login api: Takes `username` & `password` (validated with JSON db, if it exists, returns success).

- select user api: select all the user from database in json format
