import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('enable running')
@cli.command()
def start(): click.echo('enable started')
if __name__ == '__main__': cli()
