import sys
def main():
    from .application import HelloApp



    app = HelloApp(application_id="com.example.GtkApplication")
    rv = app.run(sys.argv)
    sys.exit(rv)


if __name__ == "__main__":
    # execute only if run as the entry point into the program
    main()