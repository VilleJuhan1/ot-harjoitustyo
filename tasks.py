from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def reset_score(ctx):
    ctx.run("python3 src/menu/reset_highscore.py")

@task
def autopep(ctx):
    ctx.run("autopep8 --in-place --recursive src")

@task
def devcommands(ctx):
    ctx.run("python3 src/game/devcommands.py")