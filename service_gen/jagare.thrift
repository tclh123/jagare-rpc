namespace py service_gen.jagare
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
    3: required i64 time,
    4: required i16 offset,  # Offset from UTC in minutes.
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
    3: required list<string> parents,  # shas  # 可能为空list
    4: required string tree,  # sha of the tree object attached to the commit
    5: required Signature committer,
    6: required Signature author,
    7: required string email,
    8: required string commit,
    9: required string message,
    10: required string body,  # commit message body
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

# TODO: modify this after ellen ls-tree refactor
struct LightWeightTag {
    1: required string type,  # 'commit'  ????
    2: required string name,  # short reference name
    3: required string tag,  # same as name
    4: required string object,  # tag.hex
    5: required Commit commit,
}

struct GitObject {
    1: required string type,
    2: optional Blob blob,
    3: optional Tree tree,
    4: optional Commit commit,
    5: optional Tag tag,
}

struct BlameHunk {
    1: required i32 lines_in_hunk,
    2: required string final_commit_id,
    3: required i32 final_start_line_number,
    4: required Signature final_committer,
    5: required string orig_commit_id,
    6: required string orig_path,
    7: required i32 orig_start_line_number,
    8: required bool boundary,  # Tracked to a boundary commit.
    9: required Signature orig_committer,  #  orig_committer is None

}

struct Blame {
    1: required Blob blob,
    2: required list<BlameHunk> hunks,
}

struct DiffLine {
    1: required string attr,  # char
    2: required string line,
}

struct Hunk {
    1: required i32 old_start,
    2: required i32 new_start,
    3: required i32 old_lines,
    4: required i32 new_lines,
    5: required list<DiffLine> lines,  # hunk.lines,
}

struct Patch {
    1: required string amode,
    2: required string bmode,
    3: optional string old_sha,  # commit from_sha, may be None
    4: required string new_sha,  # commit to_sha
    5: required i32 additions,
    6: required i32 deletions,
    7: required i32 similarity,
    8: required list<Hunk> hunks,
    9: required string old_oid,  # may be 0 * 40
    10: required string new_oid,
    11: required string status,  # char
    12: required bool is_binary,
    13: required string old_file_path,
    14: required string new_file_path,
}

struct Diff {
    1: optional string old_sha,  # may be None
    2: required string new_sha,
    3: required list<Patch> patches,
    4: required string patch,  # patch diff string
}

struct MergeResult {
    1: required bool is_uptodate,
    2: required bool is_fastforward,
    3: required string fastforward_oid,
}

struct MergeIndex {
    1: required bool has_conflicts,
}

exception ServiceUnavailable {
    1: string message,
}

exception NoneResult {
    1: string message,
}

service Jagare {
    Repository get(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    list<string> list_branches(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    list<string> list_remotes(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    list<string> list_tags(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    GitObject show(1:string path, 2:string ref)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    # TODO: fix retval after refactor ellen
    string ls_tree(1:string path, 2:string ref, 3:string req_path, 4:bool recursive,
                   5:bool with_size, 6:bool with_commit, 7:bool name_only)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    list<Commit> rev_list(1:string path, 2:string to_ref, 3:string from_ref,
                          4:string file_path, 5:i32 skip, 6:i32 max_count, 7:string author,
                          8:string query, 9:bool first_parent, 10:i64 since,
                          11:bool no_merges)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    Blame blame(1:string path, 2:string ref, 3:string req_path, 4:i32 lineno)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    string format_patch(1:string path, 2:string ref, 3:string from_ref)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    map<string, string> detect_renamed(1:string path, 2:string ref)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    bool commit(1:string path, 2:string branch, 3:string parent_ref,
                4:string author_name, 5:string author_email,
                6:string message, 7:string reflog, 8:list<list<string>> data)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    Diff diff(1:string path, 2:string ref, 3:string from_ref, 4:bool ignore_space,
              5:i16 flags, 6:bool context_lines, 7:list<string> paths,
              8:bool rename_detection)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    string resolve_commit(1:string path, 2:string version)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    string resolve_type(1:string path, 2:string version)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    bool create_branch(1:string path, 2:string name, 3:string ref, 4:bool force)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    bool delete_branch(1:string path, 2:string name)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    Repository clone_to(1:string path, 2:string to_path, 3:bool is_bare, 4:string branch,
                     5:bool is_mirror, 6:map<string, string> env)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    # classmethod
    Repository mirror(1:string url, 2:string to_path, 3:bool is_bare,
                      4:string branch, 5:map<string, string> env)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    # classmethod
    Repository init(1:string to_path, 2:string work_path, 3:bool is_bare)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    list<string> list_references(1:string path)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    bool add_remote(1:string path, 2:string name, 3:string url)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    bool update_ref(1:string path, 2:string ref, 3:string newvalue)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    bool update_head(1:string path, 2:string branch_name)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    string sha(1:string path, 2:string rev)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    string merge_base(1:string path, 2:string to_sha, 3:string from_sha)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    oneway void fetch_all(1:string path)

    oneway void fetch(1:string path, 2:string name)

    oneway void fetch_raw(1:string path, 2:string name, 3:bool is_q,
                          4:map<string, string> env)

    ProcessResult merge(1:string path, 2:string ref, 3:string msg, 4:string commit_msg,
                        5:bool no_ff, 6:map<string, string> env)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    MergeIndex merge_tree(1:string path, 2:string ours, 3:string theirs)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    MergeResult merge_head(1:string path, 2:string ref)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    MergeIndex merge_commits(1:string path, 2:string ours, 3:string theirs)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    string merge_flow(1:string path, 2:string merger_name, 3:string merger_email,
                      4:string message_header, 5:string message_body,
                      6:string from_repo_path, 7:string from_ref, 8:string to_ref,
                      9:string remote_name, 10:bool no_ff)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    bool can_merge(1:string path, 2:string from_repo_path,
                   3:string from_ref, 4:string to_ref, 5:string remote_name)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    ProcessResult push(1:string path, 2:string remote, 3:string ref
                       4:map<string, string> env)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),

    string archive(1:string path, 2:string prefix, 3:string ref)
        throws (
            1: ServiceUnavailable unavailable,
            2: NoneResult none_result,
        ),
}
