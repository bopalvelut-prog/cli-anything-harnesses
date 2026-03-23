import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('math running')
@cli.command()
def start(): click.echo('math started')
if __name__ == '__main__': cli()
