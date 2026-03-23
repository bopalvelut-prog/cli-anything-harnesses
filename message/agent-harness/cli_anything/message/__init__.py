import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('message running')
@cli.command()
def start(): click.echo('message started')
if __name__ == '__main__': cli()
