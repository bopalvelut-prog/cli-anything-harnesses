import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('source')
@click.argument('dest')
def copy(source, dest): subprocess.run(['rclone', 'copy', source, dest])
@cli.command()
@click.argument('source')
@click.argument('dest')
def sync(source, dest): subprocess.run(['rclone', 'sync', source, dest])
@cli.command()
def remotes(): subprocess.run(['rclone', 'listremotes'])
if __name__ == '__main__': cli()
