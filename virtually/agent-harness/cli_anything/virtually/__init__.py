import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('virtually running')
@cli.command()
def start(): click.echo('virtually started')
if __name__ == '__main__': cli()
