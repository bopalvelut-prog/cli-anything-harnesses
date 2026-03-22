import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def check(): subprocess.run(['docker-bench-security'])
if __name__ == '__main__': cli()
