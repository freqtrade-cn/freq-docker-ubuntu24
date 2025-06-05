def create_docker_compose(config):
    base_template = """
---
services:
  freqtrade{port}:
    image: freqtradeorg/freqtrade:stable
    restart: unless-stopped
    container_name: freqtrade{port}
    volumes:
      - "./user_data{port}:/freqtrade/user_data"
    # Expose api on port 8080 (localhost only)
    # Please read the https://www.freqtrade.io/en/stable/rest-api/ documentation
    # for more information.
    ports:
      - "0.0.0.0:{port}:8080"
    # Default command used when running `docker compose up`
    command: >
      trade
      --logfile /freqtrade/user_data/logs/freqtrade.log
      --db-url sqlite:////freqtrade/user_data/tradesv3.sqlite
      --config /freqtrade/user_data/config.json
      --strategy {strategy} 
"""
    for c in config:
        template = base_template.format(port=c['port'], strategy=c['strategy'])
        with open(f"docker-compose-{c['port']}.yml", "w") as f:
            f.write(template)
# 删除 user_data 之外的以 user_data 开头的文件夹
def delete_user_data_folders(config):
    import os
    import shutil
    
    for c in config:
        port = c['port']
        folder_name = f"user_data{port}"
        if os.path.exists(folder_name) and folder_name != "user_data":
            shutil.rmtree(folder_name)
            
def copy_user_data(config):
    import shutil
    import os
    
    for c in config:
        port = c['port']
        src = "user_data"
        dst = f"user_data{port}"
        
        # Create destination if it doesn't exist
        if not os.path.exists(dst):
            # Copy the entire user_data directory
            shutil.copytree(src, dst)
            
def update_config_ports(config):
    import json
    import os
    
    for c in config:
        port = c['port']
        config_path = f"user_data{port}/config.json"
        
        if os.path.exists(config_path):
            # Read the config file
            with open(config_path, 'r') as f:
                config_data = json.load(f)
            
            # Update the listen_port
            if 'api_server' in config_data:
                config_data['api_server']['listen_port'] = port
            
            # Write back the updated config
            with open(config_path, 'w') as f:
                json.dump(config_data, f, indent=4)

if __name__ == "__main__":
    config = [
        {
            "port": 8080,
            "strategy": "SampleStrategy"
        },
        {
            "port": 8081,
            "strategy": "SampleStrategy"
        },
        {
            "port": 8082,
            "strategy": "SampleStrategy"
        }
        ,
        {
            "port": 8083,
            "strategy": "SampleStrategy"
        }
        ,
        {
            "port": 8084,
            "strategy": "SampleStrategy"
        }
        ,
        {
            "port": 8085,
            "strategy": "SampleStrategy"
        }
        ,
        {
            "port": 8086,
            "strategy": "SampleStrategy"
        }
        ,
        {
            "port": 8087,
            "strategy": "SampleStrategy"
        }
    ]
    
    create_docker_compose(config)
    delete_user_data_folders(config)
    copy_user_data(config)
    update_config_ports(config)