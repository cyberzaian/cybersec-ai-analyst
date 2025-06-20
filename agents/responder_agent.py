from responder import block_ip

def respond_if_needed(ip, analysis):
    if "high" in analysis.lower():
        return block_ip(ip)
    return "No response needed"
