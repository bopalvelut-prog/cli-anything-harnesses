import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asyncapi running')
@cli.command()
def start(): click.echo('asyncapi started')
if __name__ == '__main__': cli()
