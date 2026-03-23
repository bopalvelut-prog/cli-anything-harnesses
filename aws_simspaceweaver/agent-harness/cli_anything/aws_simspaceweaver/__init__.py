import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_simspaceweaver running')
@cli.command()
def start(): click.echo('aws_simspaceweaver started')
if __name__ == '__main__': cli()
