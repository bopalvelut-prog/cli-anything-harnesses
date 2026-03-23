import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('throw running')
@cli.command()
def start(): click.echo('throw started')
if __name__ == '__main__': cli()
