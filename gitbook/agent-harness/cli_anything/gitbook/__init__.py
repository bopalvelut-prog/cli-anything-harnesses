import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('GitBook started')
@cli.command()
def build(): click.echo('GitBook built')
if __name__ == '__main__': cli()
