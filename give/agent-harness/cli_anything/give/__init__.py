import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('give running')
@cli.command()
def start(): click.echo('give started')
if __name__ == '__main__': cli()
