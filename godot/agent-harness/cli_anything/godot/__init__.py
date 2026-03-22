
import click, subprocess, os

@click.group()
def cli(): pass

@cli.command()
@click.argument('project_path')
@click.option('--script', help='Script to run')
def run(project_path, script):
    cmd = ['godot', '-path', project_path]
    if script:
        cmd.extend(['--script', script])
    subprocess.run(cmd)
    click.echo(f'Ran: {project_path}')

@cli.command()
@click.argument('project_path')
@click.option('-o', '--output', required=True)
def export(project_path, output):
    cmd = ['godot', '--headless', '-path', project_path, '--export-release', output]
    subprocess.run(cmd)
    click.echo(f'Exported: {output}')

if __name__ == '__main__':
    cli()
