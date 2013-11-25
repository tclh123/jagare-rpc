struct Repository {
    1: required string path,
    2: required bool is_empty,
    3: required bool is_bare,
    4: optional string workdir,
}

exception ServiceUnavailable {
    1: string message,
}

service Jagare {
    Repository get(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
        ),
}
