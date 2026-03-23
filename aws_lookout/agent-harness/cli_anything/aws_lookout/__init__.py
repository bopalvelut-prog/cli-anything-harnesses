import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_lookout running')
@cli.command()
def start(): click.echo('aws_lookout started')
if __name__ == '__main__': cli()
