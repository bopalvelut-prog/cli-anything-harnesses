import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def users(): click.echo('Intercom users')
@cli.command()
def conversations(): click.echo('Intercom conversations')
if __name__ == '__main__': cli()
