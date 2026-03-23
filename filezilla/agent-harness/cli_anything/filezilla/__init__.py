import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('filezilla running')
@cli.command()
def start(): click.echo('filezilla started')
if __name__ == '__main__': cli()
