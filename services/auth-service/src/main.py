from infrastructure.web_frameworks.fastapi.app import app as fastapi_app

# Entry point for the application


def main():
    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
