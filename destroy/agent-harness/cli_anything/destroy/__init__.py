import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('destroy running')
@cli.command()
def start(): click.echo('destroy started')
if __name__ == '__main__': cli()
