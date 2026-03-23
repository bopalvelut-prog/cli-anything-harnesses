import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('debate running')
@cli.command()
def start(): click.echo('debate started')
if __name__ == '__main__': cli()
