import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('source')
@click.argument('dest')
def sync(source, dest): subprocess.run(['rsync', '-avz', source, dest])
@cli.command()
@click.argument('source')
@click.argument('dest')
def dryrun(source, dest): subprocess.run(['rsync', '-avz', '--dry-run', source, dest])
if __name__ == '__main__': cli()
