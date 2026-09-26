def secure_archive(
        filename: str,
        mode: str = "r",
        content_to_write: str = ""
        ) -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(filename, 'r') as file:
                content = file.read()
                return (True, content)
        elif mode == "w":
            with open(filename, 'w') as file:
                file.write(content_to_write)
                return (True, "Content successfully written to file")
        else:
            return (False, "Invalid mode. Use 'r' for read or 'w' for write.")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", mode="r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow", mode="r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    archive = secure_archive("ancient_fragment.txt", mode="r")
    print(archive)

    if archive[0]:
        print("\nUsing 'secure_archive'" +
              " to write previous content to a new file:")
        print(secure_archive(
            "new_fragment.txt", mode="w", content_to_write=archive[1]))


if __name__ == "__main__":
    main()
