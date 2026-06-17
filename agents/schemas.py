TOOLS = [
    {
        "type": "function",
        "name": "generate_itinerary",
        "description": "Creates a travel itinerary",
        "parameters": {
            "type": "object",
            "properties": {
                "destination": {"type": "string"},
                "days": {"type": "integer"}
            },
            "required": ["destination", "days"]
        }
    }
]