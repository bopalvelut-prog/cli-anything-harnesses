import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fill running')
@cli.command()
def start(): click.echo('fill started')
if __name__ == '__main__': cli()
