struct Repository {
    1: required string path,
    2: required bool is_empty,
    3: required bool is_bare,
    4: optional string workdir,
    5: optional string head,
}

struct Author {
    1: required string name,
    2: required string email,
}

# struct Signature {
#     1: required Author author,
#     2: required string time,
#     3: required string time_offset,
# }

exception ServiceUnavailable {
    1: string message,
}

service Jagare {
    Repository get(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    list<string> list_branches(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    list<string> list_tags(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    # show, TODO: formated dict -> struct or map(JSON)?

    # ls_tree

    # rev_list, return commits list
    # def rev_list(repository, to_ref, from_ref=None, path=None, skip=0,
    #              max_count=0, author=None, query=None, first_parent=None,
    #              since=0, no_merges=None):

    # blame

    string format_patch(1:string path, 2:string ref, 3:string from_ref)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    map<string, string> detect_renamed(1:string path, 2:string ref)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    bool commit(1:string path, 2:string branch, 3:string parent_ref,
                4:string author_name, 5:string author_email,
                6:string message, 7:string reflog, 8:list<list<string>> data)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    # diff

    string resolve_commit(1:string path, 2:string version)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    string resolve_type(1:string path, 2:string version)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    bool create_branch(1:string path, 2:string name, 3:string ref, 4:bool force)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    Repository clone_to(1:string path, 2:string to_path, 3:bool is_bare, 4:string branch,
                     5:bool is_mirror, 6:map<string, string> env)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    # classmethod
    Repository mirror(1:string url, 2:string to_path, 3:bool is_bare,
                      4:string branch, 5:map<string, string> env)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    # oneway void fetch()
}
