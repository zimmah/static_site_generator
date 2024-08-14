# #!/bin/bash

# export FORCE_COLOR=1
# export CLICOLOR_FORCE=1

# python3 -m unittest discover -s src -v 2>&1 | while IFS= read -r line; do
#     if [[ $line =~ .*ok$ ]]; then
#         printf "\033[32m%s\033[0m\n" "$line"
#     elif [[ $line =~ .*FAIL.*|.*ERROR.* ]]; then
#         printf "\033[31m%s\033[0m\n" "$line"
#     elif [[ $line =~ ^Ran[[:space:]].*[[:space:]]in[[:space:]] ]]; then
#         printf "\033[34m%s\033[0m\n" "$line"  # Blue for the summary line
#     elif [[ $line =~ ^OK$ ]]; then
#         printf "\033[32m%s\033[0m\n" "$line"  # Green for the final OK
#     else
#         printf "%s\n" "$line"
#     fi
# done

#!/bin/bash

export FORCE_COLOR=1
export CLICOLOR_FORCE=1

python3 -m unittest discover -s src -v 2>&1 | while IFS= read -r line; do
    if [[ $line =~ .*ok$ ]]; then
        printf "\033[32m%s\033[0m\n" "$line"
    elif [[ $line =~ ^FAIL:|^ERROR:|FAILED|.*FAIL$ ]]; then
        printf "\033[31m%s\033[0m\n" "$line"
    elif [[ $line =~ ^====+$ ]]; then
        printf "\033[33m%s\033[0m\n" "$line"  # Yellow for separator lines
    elif [[ $line =~ ^Traceback ]]; then
        printf "\033[35m%s\033[0m\n" "$line"  # Magenta for traceback
    elif [[ $line =~ ^[[:space:]]*File ]]; then
        printf "\033[36m%s\033[0m\n" "$line"  # Cyan for file paths
    elif [[ $line =~ ^AssertionError: ]]; then
        printf "\033[31m%s\033[0m\n" "$line"  # Red for AssertionError
    elif [[ $line =~ ^- ]]; then
        printf "\033[31m%s\033[0m\n" "$line"  # Red for removed lines
    elif [[ $line =~ ^\+ ]]; then
        printf "\033[32m%s\033[0m\n" "$line"  # Green for added lines
    elif [[ $line =~ ^\? ]]; then
        printf "\033[33m%s\033[0m\n" "$line"  # Yellow for difference indicators
    elif [[ $line =~ ^Ran[[:space:]].*[[:space:]]in[[:space:]] ]]; then
        printf "\033[34m%s\033[0m\n" "$line"  # Blue for the summary line
    elif [[ $line =~ ^OK$ ]]; then
        printf "\033[32m%s\033[0m\n" "$line"  # Green for the final OK
    else
        printf "%s\n" "$line"
    fi
done