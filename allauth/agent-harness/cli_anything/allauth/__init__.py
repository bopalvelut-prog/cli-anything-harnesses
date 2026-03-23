import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('allauth running')
@cli.command()
def start(): click.echo('allauth started')
if __name__ == '__main__': cli()
