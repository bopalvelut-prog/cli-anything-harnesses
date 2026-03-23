import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alert running')
@cli.command()
def start(): click.echo('alert started')
if __name__ == '__main__': cli()
