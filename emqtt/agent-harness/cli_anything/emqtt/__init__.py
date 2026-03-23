import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('emqtt running')
@cli.command()
def start(): click.echo('emqtt started')
if __name__ == '__main__': cli()
