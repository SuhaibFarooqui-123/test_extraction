from lean_dojo import LeanGitRepo, trace

repo = LeanGitRepo("https://github.com/yangky11/lean4-example", "944e8bfe8848416ad1c2bdbfd519c79b5ae90668")
trace(repo, dst_dir="traced_lean4-example")