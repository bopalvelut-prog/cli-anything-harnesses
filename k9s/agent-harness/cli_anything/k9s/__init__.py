import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def ui(): subprocess.run(['k9s'])
@cli.command()
def info(): click.echo('k9s info')
if __name__ == '__main__': cli()
