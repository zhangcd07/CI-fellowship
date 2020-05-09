mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"zhangcd07@outlook.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml