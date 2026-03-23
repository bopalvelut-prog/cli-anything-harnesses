import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('moreover running')
@cli.command()
def start(): click.echo('moreover started')
if __name__ == '__main__': cli()
