import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('url running')
@cli.command()
def start(): click.echo('url started')
if __name__ == '__main__': cli()
