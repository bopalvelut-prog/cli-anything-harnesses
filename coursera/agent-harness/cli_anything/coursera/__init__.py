import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('coursera running')
@cli.command()
def start(): click.echo('coursera started')
if __name__ == '__main__': cli()
