import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def conversations(): click.echo('Chatwoot conversations')
@cli.command()
def agents(): click.echo('Chatwoot agents')
if __name__ == '__main__': cli()
