import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_resource_groups running')
@cli.command()
def start(): click.echo('aws_resource_groups started')
if __name__ == '__main__': cli()
