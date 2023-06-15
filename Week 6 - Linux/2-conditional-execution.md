# Conditional Execution in Bash

Condition is based on exit status of commands.

Use `$?` to check status.

If exit status is 0, `true`

```bash
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "Error! 127.0.0.1 is not in /etc/hosts"
fi
```

![](images/20230613155435.png)

`Test` a command that evaluates the conditions received and exits with zero when they're true and with one when they are false.

```bash
if test -n "$PATH"; then echo "Your path is not empty"; fi
```

```bash
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
```

`[]` alias to test command. There needs to be a space before the end bracket.