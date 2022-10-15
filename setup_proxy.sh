
toxiproxy-cli create Conclave --listen 127.0.0.01:9000 --upstream 127.0.0.1:9005 
toxiproxy-cli toxic add Conclave -t latency -n latency_upstream -a latency=500 --upstream
toxiproxy-cli toxic add Conclave -t latency -n latency_downstream -a latency=500 --downstream
toxiproxy-cli toxic add Conclave -t bandwidth -n bandwidth_upstream -a rate=5000 --upstream
toxiproxy-cli toxic add Conclave -t bandwidth -n bandwidth_downstream -a rate=5000 --downstream

