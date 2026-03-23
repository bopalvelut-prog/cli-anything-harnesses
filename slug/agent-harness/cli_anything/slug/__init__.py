import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slug running')
@cli.command()
def start(): click.echo('slug started')
if __name__ == '__main__': cli()
