import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hostel running')
@cli.command()
def start(): click.echo('hostel started')
if __name__ == '__main__': cli()
