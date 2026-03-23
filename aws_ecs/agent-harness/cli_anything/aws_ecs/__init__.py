import click
@click.group()
def cli(): pass
@cli.command()
def clusters(): click.echo('ECS clusters')
@cli.command()
def services(): click.echo('ECS services')
if __name__ == '__main__': cli()
