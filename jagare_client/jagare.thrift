struct Repository {
    1: required string path,
    2: required bool is_empty,
    3: required bool is_bare,
    4: optional string workdir,
    5: optional string head,
}

struct Signature {
    1: required string name,
    2: required string email,
    3: required string time,
    4: required string time_offset,
}

struct ProcessResult {
    1: required string stdout,
    2: required string stderr,
    3: required string fullcmd,
    4: optional i16 returncode,  # None if process hasn't terminated yet.
}

struct Blob {
    1: required string type,  # 'blob'
    2: required string sha,
    3: required string data,
    4: required i64 size,
    5: required bool is_binary,  # binary is keyword?
}

struct TreeEntry {
    1: required string type,  # in ('commit', 'blob', 'tree')
    2: required string sha,
    3: required string mode,
    4: required string path,  # entry.name
}

struct Tree {
    1: required string type,  # 'tree'
    2: required list<TreeEntry> entries,
}

struct Commit {
    1: required string type,  # 'commit'
    2: required string sha,
    3: required list<string> parents,  # shas
    4: required string tree,  # sha of the tree object attached to the commit
    5: required Signature committer,
    6: required Signature author,
    7: required string email,
    8: required string time,
    9: optional string time_offset,  # optional yet
    10: required string commit,
    11: required string message,
    12: required string body,  # commit message body
}

struct Tag {
    1: required string type,  # 'tag'
    2: required string sha,
    3: required string name,
    4: required string target,  # tag.target.sha
    5: required Signature tagger,
    6: required string message,
    7: required string body,
}

struct LightWeightTag {
    1: required string type,  # 'commit'  ????
    2: required string name,  # short reference name
    3: required string tag,  # same as name
    4: required string object,  # tag.hex
    5: required Commit commit,
}

# TODO: struct  Diff Patch Hunk


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

    list<string> list_remotes(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    list<string> list_tags(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    # TODO:
    # show
    # def show(self, ref):

    # ls_tree  # TODO: refactor ellen

    # rev_list, return commits list
    # def rev_list(repository, to_ref, from_ref=None, path=None, skip=0,
    #              max_count=0, author=None, query=None, first_parent=None,
    #              since=0, no_merges=None):

    # blame  # I give up... # TODO: refactor ellen

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

    # diff, TODO: refactor ellen

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

    bool delete_branch(1:string path, 2:string name)
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

    # classmethod
    Repository init(1:string to_path, 2:string work_path, 3:bool is_bare)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    list<string> list_references(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    bool add_remote(1:string path, 2:string name, 3:string url)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    bool update_ref(1:string path, 2:string ref, 3:string newvalue)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    bool update_head(1:string path, 2:string branch_name)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    string sha(1:string path, 2:string rev)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    string merge_base(1:string path, 2:string to_sha, 3:string from_sha)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    oneway void fetch_all(1:string path)

    oneway void fetch(1:string path, 2:string name)

    ProcessResult merge(1:string path, 2:string ref, 3:string msg, 4:string commit_msg,
                        5:bool no_ff, 6:map<string, string> env)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    ProcessResult push(1:string path, 2:string remote, 3:string ref
                       4:map<string, string> env)
        throws (
            1: ServiceUnavailable unavailable,
        ),

    string archive(1:string path, 2:string prefix, 3:string ref)
        throws (
            1: ServiceUnavailable unavailable,
        ),
}