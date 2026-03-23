import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trunk running')
@cli.command()
def start(): click.echo('trunk started')
if __name__ == '__main__': cli()
