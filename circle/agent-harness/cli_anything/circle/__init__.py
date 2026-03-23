import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('circle running')
@cli.command()
def start(): click.echo('circle started')
if __name__ == '__main__': cli()
